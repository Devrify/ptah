FROM golang:alpine3.19

ENV TAILSCALE_AUTH_KEY your-tailscale-auth-key
ENV DERP_DOMAIN your-hostname.com
ENV DERP_CERT_MODE letsencrypt
ENV DERP_CERT_DIR /app/certs
ENV DERP_ADDR :443
ENV DERP_STUN true
ENV DERP_STUN_PORT 3478
ENV DERP_HTTP_PORT 80
ENV DERP_VERIFY_CLIENTS false

RUN apk add go --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community && \
    go install tailscale.com/cmd/derper@main && \
    apk add curl iptables && \
    apk add tailscale --repository=https://dl-cdn.alpinelinux.org/alpine/edge/community && \
    tailscale up --accept-routes=true --accept-dns=true --auth-key $TAILSCALE_AUTH_KEY

CMD derper --hostname=$DERP_DOMAIN \
    --certmode=$DERP_CERT_MODE \
    --certdir=$DERP_CERT_DIR \
    --a=$DERP_ADDR \
    --stun=$DERP_STUN  \
    --stun-port=$DERP_STUN_PORT \
    --http-port=$DERP_HTTP_PORT \
    --verify-clients=$DERP_VERIFY_CLIENTS
