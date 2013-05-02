set :target_name, "staging"
role :app, "dev2.hatsutabi.georepublic.net"
role :web, "dev2.hatsutabi.georepublic.net"
role :db, "dev2.hatsutabi.georepublic.net", :primary => true
set :branch, :master
