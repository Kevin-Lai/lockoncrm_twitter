from django.shortcuts import render

from .forms import CreateTweetForm, DeleteTweetForm, UserForm
from .models import CreateTweet, DeleteTweet, User

import twitter

# Put in your own Twitter Username and Twitter API keys to authenticate
twitter_user_id = "your_twitter_username"
api = twitter.Api(consumer_key='your_consumer_key',
                  consumer_secret='your_consumer_secret_key',
                  access_token_key='your_access_key',
                  access_token_secret='your_access_secret_key')

# Create your views here.

def create_tweet_form_view(request):
	form = CreateTweetForm(request.POST or None)
	text = ''
	if form.is_valid():
		text = form.cleaned_data['description']
		form.save()
		# Post the tweet
		status = api.PostUpdate(text)
	context = {
		'form': form,
		'text': text
	}
	return render(request, "tweets/create_tweet.html", context)


def tweet_view(request):
	user_id = twitter_user_id
	user_tweets = api.GetUserTimeline(screen_name=twitter_user_id, exclude_replies=True, include_rts=False)

	form = DeleteTweetForm(request.POST or None)
	tweet_id = ''
	delete_error = ''
	if form.is_valid():
		tweet_id = form.cleaned_data['tweet_id']		
		# Delete a Tweet by typing in its ID
		try:
			api.DestroyStatus(tweet_id)
			#return HttpResponseRedirect("tweets/show_tweet.html")
		except:
			delete_error = "The Tweet you want to delete Does Not Exist. Please Try Again."
	context = {
		'form': form,
		'delete_error': delete_error,
		'user_id': user_id,
		'user_tweets': user_tweets
	}
	return render(request, "tweets/show_tweet.html", context)