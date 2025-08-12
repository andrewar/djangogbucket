# django-gbucket

A base project incorporating gcloud buckets with django, using the gcloud storage django-storages sdk [ref](https://django-storages.readthedocs.io/en/latest/backends/gcloud.html). This is meant to be a starting point for other projects that I have using gcloud buckets with django. There is adequate docuemntation, but there were
enough gotchas that I thought a working repo would be useful for my future self as well as others.

Obviously, there is limited utility in production for the repo as-is. Use and modify at your own risk.

# Roadmap
* Initial Release: import gcloud storages and setup for a bucket as the storage backend.
* Milestone: example route for uploading files stored to bucket.
* Milestone: example route for extracting file from bucket

... and that's it! After these are done, I will try to update for future versions of the google cloud storages package and django.

# To Run

To run, one must have in their env the following:

GS_BUCKET_NAME='name of the bucket you're using'
GOOGLE_APPLICATION_CREDENTIALS='/path/to/credentials.json'
GS_PROJECT_ID='yourprojectid'



# Comments

I think in general this is actually an anti-pattern. I'm encapsulating the server in a docker container, but by consuming the google storage sdk, I'm building knowledge of the system architecture into the code. This will make it more difficult to update and change the overall architecture (including a code change coupled with a devops change) any time the system is changed to a different cloud or storage backend (for instance).

An obvious place this impacts is a development env vs. prod (or staging). If the dev env is defined using django envs, then all testing is done using code paths not used in production - and the first time the prod code paths are used is *in production*.

A better pattern, in my opinion, is to abstract the storage in such a way that the configuration at the container level is handled 'correctly' in the code (similarly for the db). This way, the same code is used in all envs, and setting the correct env is all that is needed to be successful. Tools like [*gcsfuse*](https://cloud.google.com/storage/docs/cloud-storage-fuse/overview) can be useful here, but the performance can be an issue depending on the workflow. Similar issues arise with the sdk, of course - and are more difficult to evaluate, and (particularly in a large org) resolving would require coorperation between developers and devops.

Using gcloud allows one to mount the bucket in a less performance limited way, but again creates a dependency on a single cloud vendor.

The tradeoffs are yours to explore. I do find direct use of the sdk useful enough that an example configuration for my own use is valuable.