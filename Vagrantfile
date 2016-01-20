# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.define "registry" do |registry|
    registry.vm.box = "ubuntu/trusty64"
    registry.vm.box_url = "https://atlas.hashicorp.com/ubuntu/boxes/trusty64"
    registry.vm.hostname = "vagrant-registry.vm"
    registry.vm.network "private_network", ip: "192.168.56.110"
    registry.vm.synced_folder "./", "/vagrant", disabled:true
    registry.vm.provider "virtualbox" do |vb|
      vb.name = "vagrant-registry"
      vb.cpus = 1
      vb.memory = 1*1024
    end
  end

  config.vm.provision :ansible do |ansible|
    ansible.inventory_path = "vagrant-inventory.ini"
    ansible.playbook = "vagrant-playbook.yml"
    ansible.extra_vars = { user: "vagrant" }
    ansible.sudo = true
    ansible.limit = 'all'
  end

end
