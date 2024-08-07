Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/bionic64"
    config.vm.hostname = "webserver"
    config.vm.network "private_network", ip: "192.168.33.10"
    config.vm.network "forwarded_port", guest: 80, host: 8080
    config.vm.network "forwarded_port", guest: 22, host: 2222
  
    config.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
      vb.cpus = 2
    end
  
    config.vm.synced_folder ".", "/vagrant"
  
    config.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "playbook.yml"
    end
  end
  