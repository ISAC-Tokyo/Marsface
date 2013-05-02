set :target_name, "production"
role :app, "121.119.182.37"
role :web, "121.119.182.37"
role :db, "121.119.182.37", :primary => true
set :branch, "release_phase1"
