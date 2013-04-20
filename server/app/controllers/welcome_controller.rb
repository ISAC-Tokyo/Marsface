class WelcomeController < ApplicationController
  def index
    offset = rand(Image.count)
    @image = Image.first(:offset => offset)
    if @image
      @votes = @image.votes
    else
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
