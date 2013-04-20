class CreateVotes < ActiveRecord::Migration
  def change
    create_table :votes do |t|
      t.integer :user_id
      t.integer :image_id
      t.string :comment

      t.timestamps
    end
  end
end
