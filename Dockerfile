FROM node:20-slim

# The node:20-slim image already includes ca-certificates
# No additional packages needed since git is not required

# Install Claude Code globally
RUN npm install -g @anthropic-ai/claude-code && \
    npm cache clean --force

# Create a user home directory with proper permissions
# Using 1777 (sticky bit) to prevent users from deleting each other's files
RUN mkdir -p /home/user && chmod 1777 /home/user

# Set working directory
WORKDIR /workspace

# Use the claude command from PATH
ENTRYPOINT ["claude"]