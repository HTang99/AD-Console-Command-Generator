# Dota 2 Ability Draft Console Command Generator

- This is a small local Python project for building a custom Ability Draft console command with a clickable hero UI.
- This project is mostly coded by Chatgpt, prompted by FrEEz1ng.

## Files (The ones you run)

- `AD_console_command_generator.pyw` : the main app.
- `update_assets.py` : refresh hero names from Valve's official Dota 2 datafeed and download icons for offline use. Run this with python.

## Files (Other files)

- `hero_data.json` : display names, internal command names, aliases, and optional official site slugs
- `ad_ui/logic.py` : matching, ranking, and command generation
- `ad_ui/icons.py` : local icon loader (offline only)
- `ad_ui/app.py` : Tkinter UI
- `cache/icons/` : offline icon files downloaded from Valve's hero site/CDN
- `cache/update_status.json` : hero-count check status written by the updater

## First-time setup

Run the asset updater once so the UI has local icons and updater status:

```bash
python update_assets.py
```

## How to use

- You can customized the timers on top right of the app.
- You can pick heros from the buttons on the left. The search bar can handle name and most (hopefully) alias of the heros.
- After timers and heros are set, copy the command and run it in the console in game.
- Create your *LOCALLY HOSTED AD game with NO BOTS*, and start your game (If you want to preserve the order you see in this app and be the first player to pick, also disable player shuffling).
- Use the clear AD setup command to reset everything after your testing is over.

## What it does

- Enables cheats.
- Clears the old custom AD setup.
- Lets you choose the three draft timers in the UI.
  - `pre time - the time before the very first pick`
  - `per player time - the time you have for each pick`
  - `pre round time - the waiting time between each pick`
- Lets you select up to 12 heroes by clicking.
- Fills heroes in order: first 5 to Radiant, next 5 to Dire, last 2 to extra. These (at most) 12 heros forms the pool. If you pick less than 12 heros the remaining spot will be filled by random, just like usual AD games.
- Clicking a selected hero again will unselect it.
- Shows the main setup command and a separate clear-setup command.

## Notes

- The main app does not download icons at startup. It does try to verify if the local hero count matches the offical count online.
- The updater is the one that downloads stuff, mostly icons. If in the future new heros are released this *should (but obviously not tested)* be able to download their name as well as their icon..

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software in accordance with the terms of the MIT License. See the [LICENSE](LICENSE) file for the full license text.

Dota 2, hero names, and related game assets are the property of Valve. This repository only licenses the original code in this project under MIT, and does not claim ownership of third-party game content.
