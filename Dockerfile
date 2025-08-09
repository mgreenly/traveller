FROM node:20-slim

# Install useful CLI tools, Ruby, and Python
RUN apt-get update && apt-get install -y \
    # Text processing & search
    jq \
    fzf \
    silversearcher-ag \
    fd-find \
    # File operations  
    rsync \
    tree \
    coreutils \
    diffutils \
    patch \
    # System monitoring
    htop \
    lsof \
    # Network tools
    curl \
    wget \
    net-tools \
    iputils-ping \
    # Development tools
    make \
    strace \
    libc6-dev \
    binutils \
    # Archive/compression
    tar \
    gzip \
    zip \
    unzip \
    # Programming languages
    ruby-full \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Create symlinks for fd (package installs as fdfind)
RUN ln -s /usr/bin/fdfind /usr/bin/fd

# The node:20-slim image already includes ca-certificates

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