#config.vm.box_url = "https://vagrantcloud.com/ubuntu/bionic64"
config.vm.box_url = "https://app.vagrantup.com/ubuntu/boxes/bionic64"
config.ssl_verify_peer = false
config.registration.skip = true
config.vm.box = "ubuntu/bionic64"

```
if Vagrant.has_plugin?('vagrant-registration')
  config.registration.username = 'Gio998'
  config.registration.password = 'qweasdzxc'
end

# Alternatively
if Vagrant.has_plugin?('vagrant-registration')
  config.registration.org = 'Gio998'
  config.registration.activationkey = 'qweasdzxc'
end
```