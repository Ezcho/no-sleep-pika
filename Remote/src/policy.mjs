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
  return out;
}
