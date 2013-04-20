class VoteController < ApplicationController
  def create
    uid = current_user.id
    unless (Vote.find(:first, :conditions => {:image_id => params[:image_id], :user_id => uid}))
      @vote = Vote.create(:image_id => params[:image_id], :user_id => uid)
    end
    respond_to do |format|
      format.html { render :layout => false }
      format.js
    end
  end
  def update
    @vote = Vote.find(params[:id])
    @vote.comment = params[:vote][:comment]
    @vote.save
    respond_to do |format|
      format.html { render :layout => false }
      format.js
    end
  end
end
