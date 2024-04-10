# ExpressTURN App Configuration

# Service Description
SERVICE_DESCRIPTION = "ExpressTURN provides a global cloud network of TURN servers for your WebRTC applications and services."

# TURN Server Description
TURN_SERVER_DESCRIPTION = "TURN, or Traversal Using Relays around NAT, is a protocol that helps WebRTC applications traverse NATs or firewalls. It allows clients to send and receive data through a relay server. TURN is particularly useful for clients on networks that use symmetric NAT devices."

# WebRTC Description
WEBRTC_DESCRIPTION = "WebRTC, short for Web Real-Time Communication, is a technology that enables browsers and other devices to communicate with each other in real-time without the need for an intermediary. This technology can be used for various purposes such as video conferencing, file sharing, screen sharing, and broadcasting."

# Privacy and Security Benefits
PRIVACY_SECURITY_BENEFITS = "Without using TURN servers, WebRTC using another protocol called STUN, which can expose the IP address of the connecting peers, leaving users at risk of denial-of-service attacks, location compromises, or various hacks. STUN, or Session Traversal Utilities for NAT, is a protocol that allows applications to detect the presence of NATs and firewalls and determine the peer's IP address behind a NAT. By implementing a TURN server, there is no requirement for users to share personal information such as IP addresses with each other."

# Authentication Methods
AUTHENTICATION_METHODS_DESCRIPTION = "There are multiple ways to authenticate with a TURN server. ExpressTURN supports both the long-term credentials mechanism (server setting \"lt-cred-mech\") and shared secret-based authentication (server setting \"static-auth-secret\"). The shared secret authentication method is available only to Premium customers."

# Free Plan Limits
FREE_PLAN_TRAFFIC_LIMIT = 1000  # GB per month

# Supported Ports and Protocols
SUPPORTED_PORTS = [3478, 80, 443]
SUPPORTED_PROTOCOLS = ["TCP", "UDP"]

# Regional TURN Server Locations
TURN_SERVER_LOCATIONS = [
    "Americas",
    "Europe",
    "Asia",
    "Africa",
    "Oceania"
]

# Refund Policy
REFUND_POLICY_DAYS = 30  # Days for refund eligibility

# You can add more configurations as needed