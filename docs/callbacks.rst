Callbacks
=========

In the context of la_facebook, callbacks are a subclass of
la_facebook.callbacks.base.BaseFacebookCallback.

The callback is called after the user authenticates with Facebook, either for
the first time, or when returning after authentication expiration. The callback
determines what happens next, whether that be a user being created, or the
browser being redirected.

la_facebook ships with two callbacks. BaseFacebookCallback defines the key
steps that any response to a facebook auth should include, but is largely an
abstract class.  DefaultFacebookCallback is a working callback that addresses
the most common use case for basic user auth. Most projects will
probably be fine to just use this default implementation.

What the default implementation does
------------------------------------

When a new user comes to your site, and clicks on a link that calls the
la_facebook.views.facebook_login view, they are redirected to facebook
where they are authenticated and approve your app. They are then redirected
to your site and the default callback is executed. This callback fist checks
whether there is already an authenticated Django user in the session. If not
the Facebook id of the user is examined and it is determined whether they have
previously authenticated to the site by looking for database model that stores
an association between a Django user and a Facebook user.

If there exists a prior association, the expiration of that users Facebook
authentication token is updated, the Django session expiration is set to match,
and the user is logged and redirected.

If no prior association is present, a django user and its association object
are created. The default Django username consists of the facebook user's name
sluggified and concatenated with their facebook id. Any profile object, as
defined in Django's settings, is updated with any matching fields in the users
Facebook data.

Callback Reference
------------------

A callback is a view like object is called with instances of a Django request,
OAuthAccess, and OAuth20Token.

BaseFacebookCallback

__call__ is called by the view and handles the basic check of whether the user
is authenticated and dispatches to the other methods as nessasary and then
returns the response to the view and thus to the browser (usually a redirect)

fetch_user_data Not implemented.

lookup_user Not implemented.

redirect_url Checks in order: the request GET params, the session, settings for
a url to redirect to.

handle_no_user Not implemented.

handle_unauthenticated_user Not implemented.

identifier_from_data Concatenates a sluggified facebook name and user id

DefaultFacebookCallback

TODO

    fetch_user_data [DefaultFacebookCallback]
    lookup_user [DefaultFacebookCallback]
    persist [DefaultFacebookCallback]
    handle_no_user [DefaultFacebookCallback]
    login_user [DefaultFacebookCallback]
    handle_unauthenticated_user [DefaultFacebookCallback]
    update_profile_from_graph [DefaultFacebookCallback]
    create_profile [DefaultFacebookCallback]
    create_user [DefaultFacebookCallback]

