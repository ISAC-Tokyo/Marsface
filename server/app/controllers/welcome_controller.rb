class WelcomeController < ApplicationController
  def index
    offset = rand(Image.count)
    @image = Image.first(:offset => offset)
  end
end
