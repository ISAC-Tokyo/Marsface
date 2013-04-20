class AddFacebookIdToUser < ActiveRecord::Migration
  def change
    add_column :users, :fb_user_id, :string
    add_column :users, :email, :string
  end
end
