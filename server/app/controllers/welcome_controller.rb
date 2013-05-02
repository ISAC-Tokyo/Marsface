class WelcomeController < ApplicationController
  def index
    images = Image.joins("LEFT OUTER JOIN votes ON images.id = votes.user_id").find(:all)
    if (current_user)
      images.delete_if {|i| i.votes.select{|v| v.user_id == current_user.id}.count > 0}
    end
    if images.count > 0
      offset = rand(images.size)
      @image = images[offset]
      @votes = @image.votes.sort{|a,b| a.created_at <=> b.created_at}
      #@count = @image.votes.inject(0) { |sum,elem| sum + elem.num }
    else
      @image = nil
      @votes = []
      @count = 0
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
