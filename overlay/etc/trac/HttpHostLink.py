from trac.wiki.macros import WikiMacroBase

class HttpHostLink(WikiMacroBase):
    def expand_macro(self, formatter, name, args):
        """generates href link in form of proto://HTTP_HOST:port"""
        if not args:
            raise Exception('required arguments: proto, port, desc')

        proto, port, desc = args.split(",")
        host = formatter.req.environ.get("HTTP_HOST")
        return "<a href='%s://%s:%s'>%s</a>" % (proto.strip(), host,
                                                port.strip(),
                                                desc.strip())

