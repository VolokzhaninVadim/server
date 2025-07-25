# Сервер Волокжанина Вадима
[Репозитории](https://github.com/VolokzhaninVadim/server/tree/main/repos)
```{uml}
!include articles/plantuml/server.plantuml
```

# Работа с репозиторием
```bash
# For clone with submodules
git clone --recurse-submodules git@github.com:VolokzhaninVadim/server

# Add submodule
git submodule add git@<repo>

# Remove submodule
git rm -rf --cached  <submodule path>

# Update submodules
git pull --recurse-submodules

# Move submodule
git mv old/submodule new/submodule
```

# Статьи
## Сервер
1. [Зачем нужен собственный сервер в 2025?](../source/articles/server.md)
1. [Как создать загрузочную флешку?](../source/articles/loading_flash.md)
1. [Как установить Proxmox?](../source/articles/proxmox.md)
1. [Как установить Docker?](../source/articles/docker.md)
1. [Как установить драйвера Nvidia в Linux?](../source/articles/nvidia_drivers.md)
1. [Как запустить собственный git-сервер?](../source/articles/gitea.md)
1. [Как запустить свой менеджер паролей?](../source/articles/password_manager.md)
1. [Как настроить центральный менеджмент сервер для ИБП?](../source/articles/ups.md)

## Прокси
1. [Как бесплатно получить собственный домен?](../source/articles/duckdns.md)
1. [Как запустить прокси-сервер для сервисов?](../source/articles/npm.md)

## Медиа
1. [Как создать систему для просмотра торрентов?](../source/articles/lampa.md)
1. [Как просматривать медиа с торрентов?](../source/articles/torrserver.md)
1. [Как запустить сервис по поиску торрентов?](../source/articles/jackett.md)

## Облако
1. [Как запустить сервис с собственным облаком?](../source/articles/nextcloud.md)

## Умный дом
1. [Как запустить сервис по управлению умным домом?](../source/articles/homeassistant.md)
1. [Как подключить координатор для управления IoT устройствами](../source/articles/zigbee.md)
1. [Как запустить device tracking для умного дома?](../source/articles/device_tracking.md)


Создано [Sphinx](https://github.com/sphinx-doc/sphinx)