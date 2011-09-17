from foursq_api import APIGateway

# Create your views here.

def proxy( request ):
    """
    """
    #
    # Extract and validate
    if request.method != 'GET':
        return HttpResponseBadRequest( "GET calls only" )
    
    params = request.GET
    
    req_params = ['path']
    for req_param in req_params:
        if not req_param in params:
            return HttpResponseBadRequest( "Missing require field: " + req_param )
    
    #
    # Process
    path = params['path']
    get_params = dict( params )
    del get_params['path']
    
    api = APIGateway( access_token=None, client_id="", client_secret="" )
    
    response = api.query( path, get_params, userless=True )
    
    return HttpResponse( response )
