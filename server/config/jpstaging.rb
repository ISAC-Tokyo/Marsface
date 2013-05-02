set :target_name, "jpstaging"
role :app, "153.122.1.128"
role :web, "153.122.1.128"
role :db, "153.122.1.128", :primary => true
set :branch, :master
