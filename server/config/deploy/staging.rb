set :target_name, "staging"
role :app, ""
role :web, ""
role :db, "", :primary => true
set :branch, :master
