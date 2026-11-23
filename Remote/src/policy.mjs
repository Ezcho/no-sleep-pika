export const PAIR_TTL = 5 * 60 * 1000;
export const SESSION_TTL = 24 * 60 * 60 * 1000;
export const validToken = value => typeof value === 'string' && /^[A-Za-z0-9_-]{43}$/.test(value);
export const live = (room, now = Date.now()) => !!room && !room.revoked && now < room.expiresAt;
export const claimable = (room, hash, now = Date.now()) => live(room, now) && !room.viewerHash && now < room.pairUntil && room.pairHash === hash;
// Never relay arbitrary local IPC or machine paths / diagnostic messages.
export function safeStatus(value) {
  const out = {};
  for (const key of ['ok', 'sessionOn', 'monitorOn', 'busy', 'recoveryRequired', 'waitingForLid', 'lidEngaged', 'serviceRegistered']) {
    if (typeof value?.[key] === 'boolean') out[key] = value[key];
  }
  const s = value?.safety;
  out.safety = {};
  if (Number.isFinite(s?.batteryPercent) && s.batteryPercent >= 0 && s.batteryPercent <= 100) out.safety.batteryPercent = s.batteryPercent;
  for (const key of ['onAC', 'lidClosed', 'hasExternalDisplay']) if (typeof s?.[key] === 'boolean') out.safety[key] = s[key];
  if (['nominal', 'normal', 'fair', 'serious', 'critical'].includes(s?.thermalState)) out.safety.thermalState = s.thermalState;
  const p = value?.power;
  if (p && typeof p === 'object' && !Array.isArray(p)) {
    out.power = {};
    for (const key of ['acOnly','stopOnDisconnect']) if (typeof p[key] === 'boolean') out.power[key] = p[key];
    if ([0,30,40,50].includes(p.batteryFloor)) out.power.batteryFloor = p.batteryFloor;
    for (const key of ['timerAction','pendingAction']) if ([...powerActions,'none'].includes(p[key])) out.power[key] = p[key];
    for (const key of ['timerDeadline','pendingDeadline']) if (p[key] === null || (Number.isSafeInteger(p[key]) && p[key] > 0 && p[key] < 9000000000000000)) out.power[key] = p[key];
  }
  return out;
}

export const validCommandID = value => typeof value === 'string' && /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(value);
const object = value => !!value && typeof value === 'object' && !Array.isArray(value);
const exact = (value, keys) => object(value) && Object.keys(value).length === keys.length && keys.every(k => Object.hasOwn(value,k));
export const powerActions = ['release','sleep','shutdown','restart'];
export function validCommand(action,args) {
  if (['set_session','set_monitor'].includes(action)) return exact(args,['enabled']) && typeof args.enabled === 'boolean';
  if (action === 'set_conditions') return exact(args,['acOnly','stopOnDisconnect','batteryFloor']) && typeof args.acOnly === 'boolean' && typeof args.stopOnDisconnect === 'boolean' && [0,30,40,50].includes(args.batteryFloor);
  if (action === 'schedule') return exact(args,['minutes','action']) && [15,30,60,180,360].includes(args.minutes) && powerActions.includes(args.action);
  return ['cancel_timer','shutdown','restart'].includes(action) && exact(args,[]);
}
