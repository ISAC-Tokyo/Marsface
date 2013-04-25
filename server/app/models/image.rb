class Image < ActiveRecord::Base
  has_many :votes
  attr_accessible :caption, :path
  def voted?(id)
    self.votes.any? {|v| v.user.id == id}
  end
  def votedby(id)
    self.votes.each {|v| return v if v.user.id == id}
  end
end
