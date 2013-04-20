class VoteController < ApplicationController
  def create
    uid = current_user.id
    unless (Vote.find(:first, :conditions => {:image_id => params[:image_id], :user_id => uid}))
      Vote.create(:image_id => params[:image_id], :user_id => uid)
    end
    respond_to do |format|
      format.html { render :layout => false }
      format.js
    end
  end
end
