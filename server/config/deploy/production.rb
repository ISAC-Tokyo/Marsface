set :target_name, "production"
set :port, 53555
role :app, "marface.cloudapp.net"
role :web, "marface.cloudapp.net"
role :db, "marface.cloudapp.net", :primary => true
set :branch, "release"
