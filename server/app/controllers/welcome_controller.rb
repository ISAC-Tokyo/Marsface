class WelcomeController < ApplicationController
  def index
    images = Image.joins("LEFT OUTER JOIN votes ON images.id = votes.user_id").find(:all)
    images.delete_if {|i| i.votes.select{|v| v.user_id == current_user.id}.count > 0}
    if images.count > 0
      offset = rand(images.size)
      @image = images[offset]
      @votes = @image.votes
    else
      @image = nil;
      @votes = []
    end
    @voted = false;
    if (current_user)
      myid = current_user.id
      @votes.each do |v|
       if (v.user_id == myid)
         @voted = true
         @myvote = v
         break
       end
      end
    end
  end
end
