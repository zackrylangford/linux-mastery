# Problem: Basic Network Troubleshooting

## What problem does this solve?

You need to diagnose network connectivity issues, check if services are reachable, see what network connections are active, or understand your system's network configuration. Network troubleshooting is essential for figuring out why you can't connect to a server, why a service isn't accessible, or what's using your network.

## When do you encounter this?

**Real-world scenarios:**
- You can't connect to a website or server and need to know if it's your network or theirs
- A service you're running isn't accessible and you need to check if it's listening on the right port
- You need to find out what your IP address is
- You're debugging why an application can't connect to a database
- You need to see what network connections are currently active on your system
- You're checking if a specific port is open or blocked
- You need to verify your network interface configuration

## Available approaches

### 1. `ping` - Test Basic Connectivity
- **Best for:** Checking if a host is reachable and measuring response time
- **Tradeoffs:** 
  - ✅ Pros: Simple, universally available, shows if basic connectivity works
  - ❌ Cons: Some hosts block ping (ICMP), doesn't test specific ports/services
- **How to recognize it:** Look for `ping` followed by a hostname or IP address
- **AI prompt template:** 
  ```
  Show me how to check if [hostname/IP] is reachable from my system
  ```

### 2. `ss` - Socket Statistics (Modern)
- **Best for:** Seeing active network connections, listening ports, and socket information
- **Tradeoffs:**
  - ✅ Pros: Fast, modern replacement for netstat, detailed information, actively maintained
  - ❌ Cons: Newer tool (may not be on very old systems), syntax different from netstat
- **How to recognize it:** Look for `ss` with options like `-tuln`, `-tap`, `-s`
- **AI prompt template:**
  ```
  Show me how to see what ports are listening on my system
  ```

### 3. `netstat` - Network Statistics (Legacy)
- **Best for:** Seeing network connections on older systems or when you're familiar with it
- **Tradeoffs:**
  - ✅ Pros: Widely known, available on older systems, lots of documentation
  - ❌ Cons: Deprecated in favor of ss, slower, less actively maintained
- **How to recognize it:** Look for `netstat` with options like `-tuln`, `-tap`, `-r`
- **AI prompt template:**
  ```
  Show me how to check what network connections are active using netstat
  ```

### 4. `ip` - Network Configuration (Modern)
- **Best for:** Viewing and configuring network interfaces, routes, and addresses
- **Tradeoffs:**
  - ✅ Pros: Modern, powerful, replaces multiple old tools (ifconfig, route), actively maintained
  - ❌ Cons: More complex syntax, newer (may not be on very old systems)
- **How to recognize it:** Look for `ip addr`, `ip link`, `ip route`
- **AI prompt template:**
  ```
  Show me how to see my network interface configuration and IP addresses
  ```

### 5. `curl` / `wget` - Test HTTP/HTTPS Connectivity
- **Best for:** Testing if a web service is accessible and responding correctly
- **Tradeoffs:**
  - ✅ Pros: Tests actual HTTP/HTTPS, can check specific endpoints, shows response details
  - ❌ Cons: Only for HTTP/HTTPS, not for general network testing
- **How to recognize it:** Look for `curl` or `wget` followed by a URL
- **AI prompt template:**
  ```
  Show me how to test if [URL] is accessible and responding
  ```

### 6. `nc` (netcat) - Network Swiss Army Knife
- **Best for:** Testing if specific ports are open, creating simple network connections
- **Tradeoffs:**
  - ✅ Pros: Very flexible, can test any TCP/UDP port, useful for debugging
  - ❌ Cons: May not be installed by default, can be complex for advanced uses
- **How to recognize it:** Look for `nc` or `netcat` with hostname and port
- **AI prompt template:**
  ```
  Show me how to check if port [number] is open on [hostname]
  ```

## Decision tree

**Choose your approach:**
1. If you need to **check basic connectivity to a host** → Use `ping hostname`
2. If you need to **see what ports are listening** → Use `ss -tuln` or `netstat -tuln`
3. If you need to **see active connections** → Use `ss -tap` or `netstat -tap`
4. If you need to **check your IP address** → Use `ip addr` or `ip a`
5. If you need to **test a specific port** → Use `nc -zv hostname port` or `telnet hostname port`
6. If you need to **test a web service** → Use `curl -I URL` or `wget --spider URL`
7. If you need to **see routing table** → Use `ip route` or `netstat -r`

## Understanding Network Basics

### The Mental Model: Layers of Connectivity

Network troubleshooting follows layers:
1. **Physical/Link**: Is the network interface up? (`ip link`)
2. **Network**: Do you have an IP address? Can you reach other hosts? (`ip addr`, `ping`)
3. **Transport**: Are the right ports open? (`ss`, `netstat`)
4. **Application**: Is the service responding correctly? (`curl`, `wget`)

**Troubleshooting strategy**: Start at the bottom and work up. If ping doesn't work, don't bother testing HTTP yet.

### Common Port Numbers to Recognize

- **22**: SSH (secure shell)
- **80**: HTTP (web traffic)
- **443**: HTTPS (secure web traffic)
- **3306**: MySQL database
- **5432**: PostgreSQL database
- **6379**: Redis
- **8080**: Alternative HTTP (often development servers)

## Examples to recognize

### Example 1: Testing basic connectivity
```bash
ping -c 4 google.com
```

**What's happening here:**
- `ping` - Send ICMP echo requests
- `-c 4` - Send only 4 packets (count), then stop
- `google.com` - The host to test
- Shows if the host is reachable and response time
- Output includes: packets sent/received, packet loss %, min/avg/max response time
- **Without -c**: ping runs forever (use Ctrl+C to stop)

### Example 2: Checking listening ports
```bash
ss -tuln
```

**What's happening here:**
- `ss` - Socket statistics (modern tool)
- `-t` - Show TCP sockets
- `-u` - Show UDP sockets
- `-l` - Show only listening sockets (servers waiting for connections)
- `-n` - Show numeric addresses (don't resolve hostnames)
- Shows what services are listening and on which ports
- Output: Protocol, local address:port, state

### Example 3: Seeing active connections
```bash
ss -tap
```

**What's happening here:**
- `ss` - Socket statistics
- `-t` - TCP sockets
- `-a` - Show all sockets (listening and established)
- `-p` - Show process using the socket
- Shows all active network connections and what program is using them
- Useful for seeing what's connected to what
- **Note**: `-p` usually requires sudo for full information

### Example 4: Checking your IP address
```bash
ip addr show
# or shorter:
ip a
```

**What's happening here:**
- `ip addr` - Show IP addresses
- `show` - Display information (can be omitted)
- Shows all network interfaces and their IP addresses
- Look for `inet` lines for IPv4 addresses
- Common interfaces: `lo` (loopback), `eth0` (ethernet), `wlan0` (wireless)
- Also shows if interface is UP or DOWN

### Example 5: Testing a specific port
```bash
nc -zv example.com 80
```

**What's happening here:**
- `nc` - Netcat (network utility)
- `-z` - Zero-I/O mode (just scan, don't send data)
- `-v` - Verbose (show what's happening)
- `example.com 80` - Host and port to test
- Tests if port 80 is open on example.com
- Returns "succeeded" if port is open, "refused" if closed
- Great for testing if a service is accessible

### Example 6: Testing web service
```bash
curl -I https://example.com
```

**What's happening here:**
- `curl` - Transfer data from/to a server
- `-I` - Fetch headers only (HEAD request)
- `https://example.com` - URL to test
- Shows HTTP response headers (status code, server info, etc.)
- Status 200 = success, 404 = not found, 500 = server error
- Tests if web service is responding correctly

### Example 7: Checking routing table
```bash
ip route show
# or shorter:
ip r
```

**What's happening here:**
- `ip route` - Show routing table
- Shows how your system routes network traffic
- Look for `default via` line - that's your gateway (router)
- Shows which interface is used for which networks
- Useful for diagnosing routing issues

### Example 8: Finding which process uses a port
```bash
sudo ss -tlnp | grep :8080
```

**What's happening here:**
- `sudo` - Need root to see process information
- `ss -tlnp` - Show TCP listening ports with process info
- `grep :8080` - Filter for port 8080
- Shows what program is listening on port 8080
- Useful when you get "address already in use" errors
- Alternative: `sudo lsof -i :8080`

### Example 9: Checking DNS resolution
```bash
nslookup example.com
# or
dig example.com
```

**What's happening here:**
- `nslookup` or `dig` - DNS lookup tools
- `example.com` - Domain to resolve
- Shows what IP address a domain name resolves to
- Useful when you suspect DNS issues
- `dig` provides more detailed information than `nslookup`

### Example 10: Testing connectivity with timeout
```bash
ping -c 3 -W 2 192.168.1.1
```

**What's happening here:**
- `ping` - Test connectivity
- `-c 3` - Send 3 packets
- `-W 2` - Wait maximum 2 seconds for response
- `192.168.1.1` - IP to test (often your router)
- Useful for quick tests without waiting too long
- Good for scripts that need to timeout quickly

### Example 11: Checking all network interfaces
```bash
ip link show
```

**What's happening here:**
- `ip link` - Show network interfaces
- Shows physical and virtual network interfaces
- Look for `state UP` or `state DOWN`
- Shows MAC addresses
- Useful for checking if interface is enabled

### Example 12: Viewing connection statistics
```bash
ss -s
```

**What's happening here:**
- `ss -s` - Show socket statistics summary
- Displays counts of different socket types
- Shows: TCP connections, UDP sockets, etc.
- Quick overview of network activity
- Useful for monitoring overall network usage

## Try with AI

**New to AI collaboration?** Check out the [AI Prompting Guide](../../references/ai-prompting-guide.md) for detailed tips on working effectively with AI.

### How to Use AI for This Problem

**Step 1: Understand what you need**
Before asking AI, be clear about:
- What's not working? (can't connect, service not accessible, etc.)
- What are you trying to reach? (website, database, specific port?)
- What information do you need? (IP address, open ports, active connections?)

**Step 2: Use a good prompt template**

Choose based on your need:

```
Testing connectivity:
"Show me how to check if [hostname/IP] is reachable from my system"

Checking ports:
"Show me how to see what ports are listening on my system"
"Show me how to check if port [number] is open on [hostname]"

Finding IP address:
"Show me how to find my system's IP address"

Diagnosing service:
"Show me how to check if [service name] is running and what port it's using"

Testing web service:
"Show me how to test if [URL] is accessible and responding correctly"

Finding what's using a port:
"Show me how to find what process is using port [number]"
```

**Step 3: Verify the AI's solution**

Before running the command, check:
- [ ] Does it use the right tool for what you're testing?
- [ ] Will it run forever? (ping without -c, for example)
- [ ] Does it need sudo? (some network commands do)
- [ ] Is it safe to run? (network commands are generally safe)

**Step 4: Test and interpret results**

```bash
# If testing connectivity and it fails, work through layers:
ping 8.8.8.8          # Can you reach internet?
ping google.com       # Does DNS work?
curl -I https://site  # Does HTTP work?

# If checking ports, understand the output:
ss -tuln              # Look for your port in the list
# If it's there: service is listening
# If not: service isn't running or listening on different port
```

**Step 5: Understand the result**

Ask AI to explain if you don't understand:
- "What does 'Connection refused' mean?"
- "What's the difference between ss and netstat?"
- "Why do I need sudo for some network commands?"
- "What does this output mean: [paste output]"

### Practice Exercises with AI

**Exercise 1: Test basic connectivity**
- **Prompt**: "Show me how to check if google.com is reachable and measure the response time"
- **Verify**: Check that it uses ping with -c to limit packets
- **Test**: Run it and understand the output
- **Document**: Note when ping is useful vs when it's not

**Exercise 2: Find your IP address**
- **Prompt**: "Show me how to find my system's IP address"
- **Verify**: Check that it uses `ip addr` or similar
- **Test**: Run it and identify your IP in the output
- **Document**: Save this for future reference

**Exercise 3: Check what's listening**
- **Prompt**: "Show me how to see what ports are listening on my system and what programs are using them"
- **Verify**: Check for `ss -tlnp` or `netstat -tlnp` with sudo
- **Test**: Run it and identify familiar services
- **Document**: Note this pattern for troubleshooting

**Exercise 4: Test a web service**
- **Prompt**: "Show me how to test if https://example.com is responding correctly"
- **Verify**: Check for `curl -I` or similar
- **Test**: Run it and understand the HTTP status code
- **Document**: Save for testing web services

### Common AI Collaboration Patterns

**Pattern 1: Layered troubleshooting**
```
You: "I can't connect to my web server"
AI: [suggests checking if server is running]
You: "It's running. How do I check if the port is open?"
AI: [provides ss or netstat command]
You: "Port is listening. How do I test from another machine?"
AI: [provides curl or nc command]
```

**Pattern 2: Understanding error messages**
```
You: "I'm getting 'Connection refused' when trying to connect"
AI: [explains this means port is closed or service not running]
You: "How do I check if the service is running?"
AI: [provides command to check service status and listening ports]
```

**Pattern 3: Finding what's using a port**
```
You: "I'm getting 'address already in use' on port 8080"
AI: [provides command to find what's using the port]
You: "It shows process 1234. How do I stop it?"
AI: [explains how to stop the process]
```

### Verification Checklist

After getting a solution from AI:
- [ ] I understand what the command is testing
- [ ] I know how to interpret the output
- [ ] I understand what success vs failure looks like
- [ ] I know what to do if the test fails
- [ ] I can explain when to use this tool vs others

### Next Steps

1. Pick one exercise above and try it with AI
2. Run the command and understand the output
3. Try a variation to deepen understanding
4. Document the pattern in `my-knowledge/problems-i-solve.md`

**Remember**: Network troubleshooting is about working through layers. Start with basic connectivity (ping), then check ports (ss), then test the actual service (curl). Don't skip steps!

## Related problems

- [Managing processes](../managing-processes/) - Services that listen on network ports are processes
- [System monitoring](../system-monitoring/) - Network usage is part of system resources
- [Finding files](../finding-files/) - Finding network configuration files

## What to memorize vs look up

**Memorize (high-value knowledge):**
- `ping` tests basic connectivity
- `ss` or `netstat` shows ports and connections
- `ip addr` shows your IP address
- `curl` tests web services
- Common ports: 22 (SSH), 80 (HTTP), 443 (HTTPS)
- The concept: troubleshoot from bottom layer up (connectivity → ports → service)

**Look up as needed (low-value to memorize):**
- Specific flags for ss/netstat (-tuln, -tap, etc.)
- All the ip command subcommands
- Advanced curl options
- Exact syntax for nc/netcat
- Less common port numbers

## For certification prep

**LPIC-1 / CompTIA Linux+ relevant syntax to recognize:**
- `ping -c 4 hostname` - Test connectivity with packet count
- `ss -tuln` - Show listening TCP/UDP ports
- `netstat -tuln` - Legacy version of above
- `ss -tap` - Show all TCP connections with processes
- `ip addr show` or `ip a` - Show IP addresses
- `ip link show` - Show network interfaces
- `ip route show` or `ip r` - Show routing table
- `curl -I URL` - Test HTTP/HTTPS connectivity
- `nc -zv host port` - Test if port is open

*Note: You don't need to memorize exact syntax, but you should recognize what these commands do and understand basic network troubleshooting flow when you see it on an exam.*

## Common Troubleshooting Patterns

**Pattern 1: "Can't connect to website"**
1. `ping 8.8.8.8` - Can you reach internet?
2. `ping google.com` - Does DNS work?
3. `curl -I https://website` - Does the site respond?

**Pattern 2: "Service not accessible"**
1. `sudo systemctl status service` - Is service running?
2. `sudo ss -tlnp | grep port` - Is it listening on the right port?
3. `nc -zv localhost port` - Can you connect locally?
4. `nc -zv remote-ip port` - Can you connect remotely?

**Pattern 3: "Port already in use"**
1. `sudo ss -tlnp | grep :port` - What's using the port?
2. `sudo kill process-id` - Stop the process (if appropriate)
3. Or change your service to use a different port

**Pattern 4: "Slow network"**
1. `ping -c 10 gateway` - Check local network latency
2. `ping -c 10 8.8.8.8` - Check internet latency
3. `ss -s` - Check number of connections
4. `ip -s link` - Check for packet errors
