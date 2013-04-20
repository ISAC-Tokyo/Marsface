class User < ActiveRecord::Base
  has_many :votes
  attr_accessible :name, :provider, :uid, :fb_user_id, :email
  def self.find_or_create_from_auth_hash(auth_hash)
    user_data = auth_hash.extra.raw_info
    if user = User.where(:fb_user_id => user_data.id).first
      user
    else # Create a user with a stub password.
      User.create!(:uid => user_data.id, :name => user_data.name, :email => user_data.email)
    end
  end
end
