from django.shortcuts import render, render_to_response, RequestContext

def home(request):

  return render_to_response("index.html",
                            locals(),
                            context_instance= RequestContext(request))

def charts(request):

  return render_to_response("charts.html",
                            locals(),
                            context_instance= RequestContext(request))


def tables(request):

  return render_to_response("tables.html",
                            locals(),
                            context_instance= RequestContext(request))



