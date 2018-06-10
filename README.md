# Continuous Integration with Reviewboard, Jenkins and SVN

Originally forked from [docker-reviewboard](https://github.com/ikatson/docker-reviewboard).

Add webhook to trigger Jenkins-Reviewbot builds and remove ship-its from Jenkins when a build fails.

## Jenkins setup
- Assumes a build called `svn-demo`
- Need to change api token
- Instructions for setting up [Jenkins-Reviewbot](https://wiki.jenkins.io/display/JENKINS/Jenkins-Reviewbot)
    - Don't add the periodic job to poll for new reviews.

## Reviewboard setup
- Create superuser called Jenkins with API token
- Add svn repository pointing to default svn project (`http://svnserver/svn/demo`)
- Add webhook pointing to webhook server. Might need to run `ping` in container to find out
 the real hostname because reviewboard complains for some reason (e.g. `http://reviewboard_webhook_1.reviewboard_default:8081` instead of `http://reviewboard:8081`)

## webhook and svn hook setup
- need to change api token
- change Jenkins credentials in webhook
