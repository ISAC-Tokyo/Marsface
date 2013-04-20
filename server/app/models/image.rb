class Image < ActiveRecord::Base
  has_many :votes
  attr_accessible :caption, :path
end
