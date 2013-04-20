class AddPathToImages < ActiveRecord::Migration
  def change
    add_column :images, :path, :string
  end
end
