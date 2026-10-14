Source: https://no-sleep-pika.online/guide/ai-overnight-electricity-cost/
Language: en

MAC GUIDE · 2026-10-15

# Who pays the electricity bill when AI works overnight?

Estimate an eight-hour Mac session, separate your electricity bill from AI service fees, and measure your own workload instead of guessing from charger wattage.

## Two places incur costs

You leave an AI task running and go to bed. Who supplies the energy for that overnight shift?

For cloud AI, the provider’s servers perform the main model computation. Your Mac still uses power for local file operations, builds and tests. With a model running locally, the Mac also performs the model computation. These are different workloads, not fixed low-power and high-power categories.

Your home electricity bill and the service subscription or API bill are separate. A meter at your outlet does not capture the data center’s energy use.

## What could eight hours cost?

Energy in kWh equals average watts multiplied by hours, divided by 1,000. Multiply that energy by your applicable price per kWh to estimate its cost.

Consider eight hours per day for 30 days at hypothetical averages of 10, 30 and 60W. These are hypothetical inputs, not MacBook measurements or a local tariff quote. Assume USD 0.20/kWh.

At 10W: 0.08kWh over eight hours, costing 1.6 US cents. Over 30 nights: 2.4kWh, costing USD 0.48.

At 30W: 0.24kWh over eight hours, costing 4.8 US cents. Over 30 nights: 7.2kWh, costing USD 1.44.

At 60W: 0.48kWh over eight hours, costing 9.6 US cents. Over 30 nights: 14.4kWh, costing USD 2.88.

Taxes, tiers and contracts affect actual bills. The figures above are total session estimates, not extra cost relative to sleeping: measure and subtract the sleep baseline for that comparison.

## Charger wattage is not consumption

A 70W adapter does not mean a Mac continuously consumes 70W. Its output capacity is different from actual draw. Charging, displays and local builds change consumption; waiting for a response is not the same load as running code.

Turning off a display can reduce display energy, but there is no universal saving for every Mac and workload.

## Measure your actual workload

If you have a plug-in meter that records cumulative kWh, follow its instructions and measure the charger during a representative task. Record battery levels and peripherals. A reading of 0.06kWh over two hours corresponds to an average of 30W.

Extrapolating that to eight hours gives 0.24kWh only if the average load stays similar. Prefer measuring the whole task. Separately powered displays and docks are outside the charger measurement; match starting and ending battery levels when comparing runs.

## Does pika save electricity?

pika maintains work that system sleep could interrupt. It does not measure electricity or reduce AI service fees. Keeping a Mac awake can consume more energy than allowing it to sleep.

For closed-lid work, check that the helper service is running, then turn Session ON. Leave Monitor OFF if you do not need to keep the display on. Briefly close and reopen the lid to check that your task keeps running. Turn Session OFF after finishing. An awake Mac cannot resolve an AI approval prompt or a network failure by itself; pika does not automatically decide when your task is complete.

[Download pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg) · [Installation help](https://no-sleep-pika.online/install/)

## Three decisions before leaving

First, define a result and stopping condition, then verify how the tool actually stops.

Second, set usage limits or alerts where the service supports them. Compare real service charges and electricity usage; do not count an existing subscription twice as an additional expense.

Third, connect your Mac to power and use a firm, ventilated desk. Do not run the Mac inside a bag or under bedding. Keep it awake for useful work and check the result afterward.

Assumptions and sources

Written by pika’s maker. The energy formula follows Virginia Cooperative Extension; placement guidance follows Apple. Wattages and USD 0.20/kWh are illustrative assumptions, not device benchmarks, local tariffs or service pricing comparisons.

- [Virginia Cooperative Extension · Estimating appliance energy use](https://ext.vt.edu/content/pubs_ext_vt_edu/en/2901/2901-9014/2901-9014.html)

- [Apple · Mac operating temperatures](https://support.apple.com/en-us/102336)

Written by the maker of no-sleep-pika; this comparison includes our own app.

[Download pika](https://github.com/Ezcho/no-sleep-pika/releases/download/v1.0.13/pika-1.0.13.pkg)[How to keep your Mac awake: clamshell mode, caffeinate and pika →](https://no-sleep-pika.online/guide/keep-mac-awake/)[Markdown](https://no-sleep-pika.online/guide/ai-overnight-electricity-cost/index.md)
