class VoteController < ApplicationController
  def create
    uid = current_user.id
    unless (Vote.find(:first, :conditions => {:image_id => params[:image_id], :user_id => uid}))
      @vote = Vote.create(:image_id => params[:image_id], :user_id => uid, :num => 1)
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
  def thumbdown
    uid = current_user.id
    unless (Vote.find(:first, :conditions => {:image_id => params[:image_id], :user_id => uid}))
      @vote = Vote.create(:image_id => params[:image_id], :user_id => uid, :num => 0)
    end
    redirect_to :controller => :welcome
  end
end
