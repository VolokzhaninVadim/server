# Сервер Волокжанина Вадима
[Репозитории](https://github.com/VolokzhaninVadim/server/tree/main/repos)
```{uml}
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Deployment.puml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

' LAYOUT_WITH_LEGEND()

!procedure $CreateTag ($alias, $description="")
    AddElementTag($alias, $legendText=$description, $sprite=%string("img:../_images/100x100/"+$alias+".png{scale=0.5}"))
!endprocedure

$CreateTag(firefox, "Firefox")
$CreateTag(tplink, "TP-Link")
$CreateTag(pikvm, "PiKVM")
$CreateTag(nut, "NUT")
$CreateTag(proxmox, "Proxmox")
$CreateTag(ubuntu, "Ubuntu")
$CreateTag(pihole, "PiHole")
$CreateTag(npm, "Nginx Proxy Manager")
$CreateTag(duckdns, "DuckDNS")
$CreateTag(tor, "TOR")
$CreateTag(home_assistant, "home_assistant")
$CreateTag(vscode, "VSCode")
$CreateTag(node_red, "Node-RED")
$CreateTag(mosquitto, "Mosquitto")
$CreateTag(zigbee2mqtt, "Zigbee2mqtt")
$CreateTag(nextcloud, "Nextcloud")
$CreateTag(syncthing, "Syncthing")
$CreateTag(gitea, "Gitea")
$CreateTag(davmail, "DavMail")
$CreateTag(redis, "Redis")
$CreateTag(elasticsearch, "Elasticsearch")
$CreateTag(homepage, "Homepage")
$CreateTag(photoprism, "Photoprism")
$CreateTag(steam, "Steam")
$CreateTag(calibre, "Calibre")
$CreateTag(transmission, "Transmission")
$CreateTag(torrserver, "Torrserver")
$CreateTag(jellyfin, "Jellyfin")
$CreateTag(jackett, "Jackett")
$CreateTag(lampa, "Lampa")

title "Сервер Волокжанина Вадима"

Person(users, "Пользователи сервисов")
System_Ext(browser, "Браузер пользователя", "Просмотр web-контента", $tags="firefox")
System_Ext(tplink, "Роутер", "Маршрутизация трафика", $tags="tplink")
System(pikvm, "KVM", "Удаленное управление через web-браузер", $tags="pikvm")
System(ups, "UPS", "Мониторинг UPS", $tags="nut")


AddProperty("vCPU", "6")
AddProperty("RAM GB", "94")
AddProperty("SSD GB (System)", "2 * 512 [ZFS RAID 1]")
AddProperty("HDD TB (VMs)", "2 * 12 [ZFS RAID 1]")
AddProperty("HDD TB (Сache VMs)", "128 GB SSD ")
AddProperty("HDD TB (Backups)", "8 [ZFS Single disk]")
AddProperty("NIC", "1")
AddProperty("Graphic card (NVidia)", "1")
Deployment_Node(server, "Сервер Волокжанина Вадима", $tags="proxmox") {

  Deployment_Node(backup-server, "Сервер резервных копий", "VM", "", $tags="proxmox"){
}

  Deployment_Node(smart-home, "Умный дом", "VM", "Docker", $tags="ubuntu"){
    Component(home_assistant, "Home Assistant", "Умный дом", "Управление умным домом", $tags="home_assistant")
    Component(vscode, "VSCode server", "VSCode server", "Написание и редактирование кода", $tags="vscode")
    Component(node_red, "Node-RED", "Node-RED", "Визуальное программирование автоматизаций", $tags="node_red")
    Component(mosquitto, "Mosquitto", "Mosquitto", "Брокер сообщений для умного дома", $tags="mosquitto")
    Component(mosquzigbee2mqttitto, "Zigbee2mqtt", "Zigbee2mqtt", "Zigbee сообщения в MQTT сообщения", $tags="zigbee2mqtt")
    Component(homepage, "Homepage", "Homepage", "Приборная панель для сервисов сервера", $tags="homepage")
}

  Deployment_Node(proxy, "Проксирование web-запросов", "VM", "Docker", $tags="ubuntu"){
    Component(pihole, "PiHole", "PiHole", "Локальный DNS-сервер с функцией блокировки рекламы", $tags="pihole")
    Component(npm, "Nginx Proxy Manager", "Nginx Proxy Manager", "Проксирование web-запросов на сервер", $tags="npm")
    Component(duckdns, "DuckDNS", "DuckDNS", "DDNS", $tags="duckdns")
    Component(tor, "TOR", "TOR", "Проксирование web-запросов от сервера", $tags="tor")
}

  Deployment_Node(cloud, "Облако", "VM", "Docker", $tags="ubuntu"){
    Component(nextcloud, "Nextcloud", "Nextcloud", "Частное облако", $tags="nextcloud")
    Component(redis, "Redis", "Redis", "Кэширование запросов в облако", $tags="redis")
    Component(elasticsearch, "Elasticsearch", "Elasticsearch", "Поиск по тексту", $tags="elasticsearch")
    Component(syncthing, "Syncthing", "Syncthing", "Синхронизация файлов между сервером и устройствами", $tags="syncthing")
    Component(gitea, "Gitea", "Gitea", "Git-сервер с функцией зеркалирования репозиториев Github", $tags="gitea")
    Component(davmail, "DavMail", "DavMail", "POP/IMAP/SMTP/Caldav/Carddav/LDAP шлюз для перевода в Carddav и Caldav", $tags="davmail")
}

  Deployment_Node(mediaserver, "Медиа сервер", "VM", "Docker", $tags="ubuntu"){
    Component(photoprism, "Photoprism", "Photoprism", "Сервис для хранения личных фото/видео c AI", $tags="photoprism")
    Component(steam, "Steam", "Steam", "Игровой сервер", $tags="steam")
    Component(calibre, "Calibre", "Calibre", "Электронная библиотека", $tags="calibre")
    Component(transmission, "Transmission", "Transmission", "Торрент-качалка", $tags="transmission")
    Component(torrserver, "Torrserver", "Torrserver", "Просмотр торррентов on-line с функцией DLNA", $tags="torrserver")
    Component(jellyfin, "Jellyfin", "Jellyfin", "Медиасервер", $tags="jellyfin")
    Component(jackett, "Jackett", "Jackett", "Торрент-поиск", $tags="jackett")
    Component(lampa, "Lampa", "Lampa", "Медиасервер для торрентов", $tags="lampa")
}
}

Rel(users, browser, "Просмотр Web-страниц")
Rel(browser, tplink, "Web-запросы")
Rel(tplink, pikvm, "Web-запросы")
Rel(tplink, server, "Web-запросы")
Rel(pikvm, server, "Управление")
Rel(ups, server, "Электричество")
Rel(server, ups, "Сигналы от автоматизаций")

' SHOW_LEGEND()

@enduml
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
1. [Как установить Proxmox?](../source/articles/proxmox.md)
1. [Как установить Docker?](../source/articles/docker.md)
1. [Как установить драйвера Nvidia в Linux?](../source/articles/nvidia_drivers.md)

## Умный дом
1. [Как запустить сервис по управлению умным домом?](../source/articles/homeassistant.md)
1. [Как подключить координатор для управления IoT устройствами](../source/articles/zigbee.md)

Создано [Sphinx](https://github.com/sphinx-doc/sphinx)