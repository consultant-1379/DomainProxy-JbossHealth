#/bin/bash
PUSHGATEWAY=$1
INSTANCE=$2
curl -g "http://$PUSHGATEWAY:8090/api/v1/series?" --data-urlencode "match[]=up{instance=\"$INSTANCE:80\"}" | cut -d: -f7 | sed s/}]}//g | sed s/\"//g


