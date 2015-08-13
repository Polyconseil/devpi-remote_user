from devpi_server.log import threadlog


def devpiserver_get_credentials(request):
    """Search request for REMOTE_USER header.

    Returns a tuple with (REMOTE_USER, '') if credentials could be
    extracted, or None if no credentials were found.

    The first plugin to return credentials is used, the order of plugin
    calls is undefined.
    """
    if 'REMOTE_USER' in request.headers:
        remote_user = request.headers['REMOTE_USER']
        threadlog.info("Found REMOTE_USER in request: %s", remote_user)
        return remote_user, ''


def devpiserver_auth_user(userdict, username, password):
    """Since we accept all remote_user, no password checks are needed."""
    threadlog.info("devpi-remoteuser accepting user: %s", username)
    return {'status': 'ok', 'groups': ['remote_user']}
