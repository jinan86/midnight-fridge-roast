# Midnight Fridge Roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/jinan86/midnight-fridge-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/jinan86/midnight-fridge-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7)

Entry for the [make.fun bounty "Midnight Fridge Roast"](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7): one line roasting a smart fridge that refuses to open after midnight. The winning roast becomes the fridge's official midnight apology note.

## The entry

> My fridge locks at midnight, then texts the whole house: "Snack attempt logged at 00:03. Judgment pending."

107 characters, one line. The joke: the fridge is not a kitchen appliance after midnight — it is a small overzealous security guard. It locks the door, files an incident report, and notifies the entire household, and the punchline is that your midnight snack is now a case awaiting judgment.

## How it works

`main.py` (Python 3, stdlib only, fully deterministic) writes the entry to `/output/entry.txt`. No input, no network, no randomness — the same bytes on every run.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
