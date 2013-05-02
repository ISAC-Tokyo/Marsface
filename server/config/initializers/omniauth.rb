Rails.application.config.middleware.use OmniAuth::Builder do
  if Rails.env.production?
    provider :facebook,"161768323988976","1c70c872560440dd3cb0598ecf27df0a"
  else
    provider :facebook,"144327189083075","51f2fdc4d6ad40985360b881329770a4"
  end
end
