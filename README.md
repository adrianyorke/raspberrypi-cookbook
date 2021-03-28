# <img src="img/Raspberry%20Pi%20Logo/Colour/Screen/PNG/RPi-Logo-SCREEN.png" width="100"/><br>raspberrypi-cookbook
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

A curated list of Raspberry Pi recipes to help beginner and intermediate Raspberry Pi enthusiasts configure Pi devices and build their projects.

# Other useful resources
* [Raspberry Pi Foundation](https://www.raspberrypi.org/)
* [Hardware - Official Products](https://www.raspberrypi.org/products/)
* [Software - Raspberry Pi OS (previously called Raspbian)](https://www.raspberrypi.org/software/)

# Table of Contents
1. Basic Configuration<br>
   * [Recipe 1.1 - enabling ssh access before first boot](src/section_01/recipe_01_01.md)<br>
     Windows:
     > ```bash
     > $ type nul > ssh
     > ```
   * [Recipe 1.2 - Assigning Static IP Address](src/section_01/recipe_01_02.md)<br>
     https://www.raspberrypi.org/documentation/configuration/tcpip/
     > ```bash
     > $ sudo nano /etc/dhcpcd.conf
     > Add the following details:
     > interface eth0
     > static ip_address=192.168.10.???/24
     > static routers=192.168.10.1
     > static domain_name_servers=127.0.0.1
     > ```
   * [Recipe 1.3 - Change VNC Cursor from X to Left Arrow](src/section_01/recipe_01_03.md)<br>
     https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=122386&p=861126
     > ```bash
     > $ cd ~
     > $ echo "xsetroot -cursor_name left_ptr&" >> .xsessionrc
     > $ sudo reboot
     > ```

1. More Advanced Configuration<br>
   * [Recipe 2.1 - Overclocking](src/section_02/recipe_02_01.md)<br>
   * [Recipe 2.2 - Running a script at boot using /etc/rc.local](src/section_02/recipe_02_02.md)<br>
   * [Recipe 2.3 - Running a scheduled script using cron](src/section_02/recipe_02_03.md)<br>

1. Basic Projects<br>
   * [Recipe 98.1 - Flashing LED](src/section_98/recipe_98_01.md)<br>
   * [Recipe 98.2 - Simple database class for recording sensor readings](src/section_98/recipe_98_02.md)<br>

1. More Advanced Projects<br>
   * [Recipe 99.1 - Magic Mirror](src/section_99/recipe_99_01.md)<br>

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/adrianyorke"><img src="https://avatars.githubusercontent.com/u/30093433?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Adrian Yorke</b></sub></a><br /><a href="#maintenance-adrianyorke" title="Maintenance">🚧</a> <a href="https://github.com/adrianyorke/raspberrypi-cookbook/commits?author=adrianyorke" title="Code">💻</a> <a href="https://github.com/adrianyorke/raspberrypi-cookbook/commits?author=adrianyorke" title="Documentation">📖</a> <a href="#ideas-adrianyorke" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/adrianyorke/raspberrypi-cookbook/pulls?q=is%3Apr+reviewed-by%3Aadrianyorke" title="Reviewed Pull Requests">👀</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
