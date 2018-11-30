#!/bin/bash
definir()
{
  read -p "Insira o IP do Gateway:      (Enter para default: 10.19.47.1)   " routerip
  routerip=${routerip:-10.19.47.1}
  read -p "Insira a mascara da rede:    (Enter para default: 255.255.255.0) " netmask
  netmask=${netmask:-255.255.255.0}
  read -p "Insira o IP desejado:        (Formato 10.19.47.55)  " staticip
  read -p "Insira o DNS desejado:       (Enter para default: 8.8.8.8)  " dns1
  dns1=${dns1:-8.8.8.8}
  read -p "Insira o Hostname desejado: (Enter para default)" hostname
  hostname="$(cat /etc/hostname)"
  read -p "Insira o nome do dispositivo (interface de rede/ Enter para default: eth0): " dev
  dev=${dev:-eth0}
  file="/etc/sysconfig/network-scripts/ifcfg-$dev"
  read -p "Insira o MAC address desejado (Enter para default): " mac
  mac="$(cat /sys/class/net/$dev/address)"
}
alterar()
{
  echo "IPADDR=$staticip" >> $file
  echo "NETMASK=$netmask" >> $file
  echo "GATEWAY=$routerip" >> $file
  echo "DNS1=$dns1" >> $file
  echo "$hostname" > /etc/hostname
  sed -i 's/ONBOOT=no.*/ONBOOT=yes/' $file
  sed -i 's/BOOTPROTO=dhcp.*/BOOTPROTO=static/' $file
  sed -i 's/HWADDR=123.*/HWADDR='$mac'/' $file
  `systemctl stop firewalld`
  `systemctl disable firewalld`
  `setenforce 0`
  sed -i 's/SELINUX=enforcing.*/SELINUX=disabled/' /etc/selinux/config
  systemctl restart network
  ####################################################
  #### Incluir mais comandos aqui!^.^!
  ####################################################
  echo "Foram feitas as seguintes alteracoes:"
  echo ""
  echo "IPADDR=$staticip em $file"
  echo "NETMASK=$netmask em $file"
  echo "GATEWAY=$routerip em $file"
  echo "MacAdress=$mac em $file"
  echo "DNS1=$dns1 em $file"
  echo "$hostname em /etc/hostname"
  echo "Desabilitado o Firewall e o Selinux"
  exit 0
}
definir
{
echo ""
echo "Suas configuracoes sao: "
echo "Gateway da rede:   $routerip"
echo "Mascara da rede:   $netmask"
echo "IP do servidor:    $staticip"
echo "Hostname	 $hostname"
echo "DNS:               $dns1"
echo "MacAdress:         $mac"
echo ""
}
while true; do
  read -p "Essas informacoes estao corretas? [y/n]: " yn
  case $yn in
    [Yy]* ) alterar $file;;
    [Nn]* ) definir;;
        * ) echo "Ecolha y or n!";;
  esac
done
