class Vote < ActiveRecord::Base
  belongs_to :user
  belongs_to :image
  attr_accessible :comment, :image_id, :user_id, :num
  def vto_s
    (num == 1) ? "+" : "-"
  end
end
