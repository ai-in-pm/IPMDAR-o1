document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatMessages = document.getElementById('chat-messages');
    const agentItems = document.querySelectorAll('.agent-item');
    const selectedAgentAvatar = document.querySelector('.selected-agent-avatar');
    const selectedAgentName = document.querySelector('.selected-agent-info h4');
    const selectedAgentDescription = document.querySelector('.selected-agent-info p');
    
    // Current selected agent
    let currentAgent = 'all';
    
    // Certification status data
    let certificationData = {};
    
    // Icons for each agent type
    const agentIcons = {
        'all': 'bi-people-fill',
        'compliance': 'bi-shield-check',
        'data_analytics': 'bi-graph-up',
        'project_management': 'bi-kanban',
        'risk_forecasting': 'bi-exclamation-triangle',
        'systems_integration': 'bi-gear-wide-connected',
        'implementation_support': 'bi-life-preserver'
    };
    
    // Agent display names
    const agentNames = {
        'all': 'All Experts',
        'compliance': 'Dr. Compliance & Policy',
        'data_analytics': 'Dr. Data Analytics',
        'project_management': 'Dr. Project Management',
        'risk_forecasting': 'Dr. Risk & Forecasting',
        'systems_integration': 'Dr. Systems Integration',
        'implementation_support': 'Dr. Implementation Support'
    };
    
    // Agent descriptions
    const agentDescriptions = {
        'all': 'Consulting the entire expert panel',
        'compliance': 'IPMDAR regulations & DoD policies',
        'data_analytics': 'Performance data & EVM metrics',
        'project_management': 'IPMDAR tailoring & implementation',
        'risk_forecasting': 'Predictive analytics & risk mitigation',
        'systems_integration': 'Technical integration & JSON formatting',
        'implementation_support': 'Step-by-step guidance & assistance'
    };
    
    // Competition mode toggle
    let competitionMode = false;
    
    // Fetch certification status for all agents
    fetchCertificationStatus();
    
    // Handle agent selection
    agentItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all agents
            agentItems.forEach(agent => agent.classList.remove('active'));
            
            // Add active class to selected agent
            this.classList.add('active');
            
            // Update current agent
            currentAgent = this.dataset.agent;
            
            // Update header with selected agent info
            updateSelectedAgentInfo(currentAgent);
            
            // Update certification details in the header if not "all"
            if(currentAgent !== 'all') {
                updateCertificationDetails(currentAgent);
            } else {
                // Hide certification details for "all" agents
                document.querySelector('.selected-agent-certification').innerHTML = '';
            }
        });
    });
    
    // Function to update the selected agent info in the header
    function updateSelectedAgentInfo(agentId) {
        // Update icon
        selectedAgentAvatar.innerHTML = `<i class="bi ${agentIcons[agentId]}"></i>`;
        
        // Update class for team or individual agent
        if (agentId === 'all') {
            selectedAgentAvatar.classList.add('team');
        } else {
            selectedAgentAvatar.classList.remove('team');
        }
        
        // Update name and description
        selectedAgentName.textContent = agentNames[agentId];
        selectedAgentDescription.textContent = agentDescriptions[agentId];
    }
    
    // Function to fetch certification status
    function fetchCertificationStatus() {
        fetch('/api/training/status')
            .then(response => response.json())
            .then(data => {
                certificationData = data;
                updateCertificationBadges();
            })
            .catch(error => {
                console.error('Error fetching certification status:', error);
            });
    }
    
    // Function to update certification badges on all agents
    function updateCertificationBadges() {
        // For each agent item (except "all")
        agentItems.forEach(item => {
            const agentId = item.dataset.agent;
            if (agentId !== 'all') {
                const agentData = certificationData[agentId];
                
                // Remove any existing badge
                const existingBadge = item.querySelector('.certification-badge');
                if (existingBadge) {
                    existingBadge.remove();
                }
                
                // Create certification badge
                const badge = document.createElement('div');
                badge.className = 'certification-badge certification-tooltip';
                
                if (agentData && agentData.certified) {
                    badge.innerHTML = '<i class="bi bi-check-lg"></i>';
                    
                    // Add tooltip with certification details
                    const tooltipContent = document.createElement('span');
                    tooltipContent.className = 'tooltip-content';
                    tooltipContent.innerHTML = `
                        <strong>Certified Agent</strong><br>
                        Score: ${agentData.final_score}%<br>
                        ${agentData.certification_date ? `Certified on: ${new Date(agentData.certification_date).toLocaleDateString()}` : ''}
                    `;
                    badge.appendChild(tooltipContent);
                } else if (agentData && agentData.training_in_progress) {
                    badge.className += ' pending';
                    badge.innerHTML = '<i class="bi bi-hourglass-split"></i>';
                    
                    // Add tooltip with pending status
                    const tooltipContent = document.createElement('span');
                    tooltipContent.className = 'tooltip-content';
                    tooltipContent.innerHTML = `
                        <strong>Training in Progress</strong><br>
                        Current progress: ${agentData.progress || 0}%
                    `;
                    badge.appendChild(tooltipContent);
                } else {
                    badge.className += ' not-certified';
                    badge.innerHTML = '<i class="bi bi-x-lg"></i>';
                    
                    // Add tooltip with not certified status
                    const tooltipContent = document.createElement('span');
                    tooltipContent.className = 'tooltip-content';
                    tooltipContent.innerHTML = `
                        <strong>Not Certified</strong><br>
                        This agent has not completed required training
                    `;
                    badge.appendChild(tooltipContent);
                }
                
                // Append badge to agent item
                item.appendChild(badge);
            }
        });
    }
    
    // Function to update certification details in the header
    function updateCertificationDetails(agentId) {
        const certContainer = document.querySelector('.selected-agent-certification') || 
                             document.createElement('div');
        
        if (!document.querySelector('.selected-agent-certification')) {
            certContainer.className = 'selected-agent-certification';
            document.querySelector('.selected-agent-info').appendChild(certContainer);
        }
        
        const agentData = certificationData[agentId];
        
        if (agentData && agentData.certified) {
            certContainer.innerHTML = `
                <div class="certification-details">
                    <span><i class="bi bi-award text-success"></i> Certified</span>
                    <span class="certification-score">${agentData.final_score}%</span>
                    ${agentData.certification_date ? 
                        `<div class="certification-date">Certified on: ${new Date(agentData.certification_date).toLocaleDateString()}</div>` : 
                        ''}
                </div>
            `;
        } else if (agentData && agentData.training_in_progress) {
            certContainer.innerHTML = `
                <div class="certification-details">
                    <span><i class="bi bi-hourglass-split text-warning"></i> Training in Progress</span>
                    <span class="certification-score">${agentData.progress || 0}%</span>
                </div>
            `;
        } else {
            certContainer.innerHTML = `
                <div class="certification-details">
                    <span><i class="bi bi-x-circle text-danger"></i> Not Certified</span>
                    <button class="btn btn-sm btn-outline-primary mt-2 start-training-btn" data-agent="${agentId}">
                        <i class="bi bi-mortarboard"></i> Start Training
                    </button>
                </div>
            `;
            
            // Add event listener to the training button
            setTimeout(() => {
                const trainingBtn = document.querySelector(`.start-training-btn[data-agent="${agentId}"]`);
                if (trainingBtn) {
                    trainingBtn.addEventListener('click', function() {
                        startAgentTraining(agentId);
                    });
                }
            }, 0);
        }
    }
    
    // Function to start agent training
    function startAgentTraining(agentId) {
        // Show loading state
        const certContainer = document.querySelector('.selected-agent-certification');
        certContainer.innerHTML = `
            <div class="certification-details">
                <span><i class="bi bi-arrow-repeat text-primary spinning"></i> Initiating training...</span>
            </div>
        `;
        
        // Call the training API
        fetch('/api/training/train', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                agent_id: agentId,
                force_retrain: true
            })
        })
        .then(response => response.json())
        .then(data => {
            // Refresh certification data
            fetchCertificationStatus();
            
            // Show success message
            addSystemMessage(
                "Training Completed", 
                `${agentNames[agentId]} has completed training with a score of ${data.details.final_score}%.`
            );
            
            // Update the certification details
            updateCertificationDetails(agentId);
        })
        .catch(error => {
            console.error('Error starting training:', error);
            certContainer.innerHTML = `
                <div class="certification-details">
                    <span><i class="bi bi-exclamation-triangle text-danger"></i> Training failed</span>
                    <button class="btn btn-sm btn-outline-primary mt-2 start-training-btn" data-agent="${agentId}">
                        <i class="bi bi-arrow-clockwise"></i> Retry
                    </button>
                </div>
            `;
            
            // Re-add event listener
            setTimeout(() => {
                const trainingBtn = document.querySelector(`.start-training-btn[data-agent="${agentId}"]`);
                if (trainingBtn) {
                    trainingBtn.addEventListener('click', function() {
                        startAgentTraining(agentId);
                    });
                }
            }, 0);
        });
    }
    
    // Auto resize textarea as user types
    userInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
        // Reset if empty
        if (this.value === '') {
            this.style.height = 'auto';
        }
    });
    
    // Handle form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const userMessage = userInput.value.trim();
        
        if (userMessage) {
            // Add user message to chat
            addUserMessage(userMessage);
            
            // Clear input field and reset height
            userInput.value = '';
            userInput.style.height = 'auto';
            
            // Scroll to bottom
            scrollToBottom();
            
            // Add typing indicator
            addTypingIndicator(currentAgent);
            
            // Send message to backend
            sendMessage(userMessage, currentAgent);
        }
    });
    
    // Function to add user message to chat
    function addUserMessage(message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'user-message';
        messageElement.innerHTML = `
            <div class="user-message-content">
                ${escapeHtml(message)}
            </div>
        `;
        chatMessages.appendChild(messageElement);
    }
    
    // Function to add agent message to chat
    function addAgentMessage(agentId, agentName, message, accuracy) {
        // Remove typing indicator if present
        removeTypingIndicator();
        
        const messageElement = document.createElement('div');
        messageElement.className = 'agent-message';
        
        // Convert message text to markdown
        const formattedMessage = marked.parse(message);
        
        messageElement.innerHTML = `
            <div class="agent-message-avatar">
                <i class="bi ${agentIcons[agentId]}"></i>
            </div>
            <div class="agent-message-content">
                <h5>${agentName}</h5>
                <div>${formattedMessage}</div>
                <div class="accuracy-rating">Accuracy Rating: ${accuracy}</div>
            </div>
        `;
        chatMessages.appendChild(messageElement);
        
        // Scroll to bottom
        scrollToBottom();
    }
    
    // Function to add multi-agent panel response
    function addMultiAgentResponse(responses) {
        // Remove typing indicator if present
        removeTypingIndicator();
        
        const responseElement = document.createElement('div');
        responseElement.className = 'multi-agent-response';
        
        let responseHtml = '<h4>Expert Panel Response</h4>';
        
        responses.forEach(response => {
            // Convert message text to markdown
            const formattedMessage = marked.parse(response.response);
            
            responseHtml += `
                <div class="multi-agent-item">
                    <h5>${agentNames[response.agent]}</h5>
                    <div>${formattedMessage}</div>
                    <div class="accuracy-rating">Accuracy Rating: ${response.accuracy}</div>
                </div>
            `;
        });
        
        responseElement.innerHTML = responseHtml;
        chatMessages.appendChild(responseElement);
        
        // Scroll to bottom
        scrollToBottom();
    }
    
    // Function to add typing indicator
    function addTypingIndicator(agentId) {
        const indicatorElement = document.createElement('div');
        indicatorElement.className = 'typing-indicator';
        indicatorElement.id = 'typing-indicator';
        
        indicatorElement.innerHTML = `
            <div class="typing-indicator-avatar">
                <i class="bi ${agentIcons[agentId]}"></i>
            </div>
            <div class="typing-indicator-content">
                <div class="typing-dots">
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                    <div class="typing-dot"></div>
                </div>
            </div>
        `;
        
        chatMessages.appendChild(indicatorElement);
        scrollToBottom();
    }
    
    // Function to remove typing indicator
    function removeTypingIndicator() {
        const indicator = document.getElementById('typing-indicator');
        if (indicator) {
            indicator.remove();
        }
    }
    
    // Function to send message to backend
    function sendMessage(message, agentId) {
        if (competitionMode) {
            handleCompetitionQuery(message);
        } else {
            fetch('/api/query', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    query: message,
                    agent: agentId
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    // Handle error
                    addSystemMessage('Error', data.error);
                } else if (data.responses) {
                    // Multi-agent response
                    addMultiAgentResponse(data.responses);
                } else {
                    // Single agent response
                    addAgentMessage(agentId, agentNames[agentId], data.response, data.accuracy);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                addSystemMessage('Error', 'Failed to get a response. Please try again.');
                removeTypingIndicator();
            });
        }
    }
    
    // Function to add system message
    function addSystemMessage(title, message) {
        const messageElement = document.createElement('div');
        messageElement.className = 'system-message';
        messageElement.innerHTML = `
            <h4>${title}</h4>
            <p>${message}</p>
        `;
        chatMessages.appendChild(messageElement);
        
        // Scroll to bottom
        scrollToBottom();
    }
    
    // Function to scroll chat to bottom
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Function to escape HTML
    function escapeHtml(unsafe) {
        return unsafe
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
    
    // Initialize auto-resize for textarea
    userInput.addEventListener('focus', function() {
        window.addEventListener('keydown', handleKeyDown);
    });
    
    userInput.addEventListener('blur', function() {
        window.removeEventListener('keydown', handleKeyDown);
    });
    
    // Handle Enter key to submit (Shift+Enter for new line)
    function handleKeyDown(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            chatForm.dispatchEvent(new Event('submit'));
        }
    }
    
    // Add competition mode toggle button
    const agentHeader = document.querySelector('.agent-header');
    const competitionToggle = document.createElement('div');
    competitionToggle.className = 'competition-toggle';
    competitionToggle.innerHTML = `
        <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" id="competitionModeToggle">
            <label class="form-check-label" for="competitionModeToggle">Competition Mode</label>
            <i class="bi bi-info-circle competition-info-icon" title="In Competition Mode, AI agents race to respond first and analyze each other's responses for accuracy."></i>
        </div>
        <div id="competition-dashboard" class="competition-dashboard" style="display: none;">
            <h5>Agent Performance Dashboard</h5>
            <div class="performance-metrics">
                <div class="metrics-container">
                    <div class="response-times-chart">
                        <canvas id="responseTimesChart"></canvas>
                    </div>
                    <div class="win-rate-chart">
                        <canvas id="winRateChart"></canvas>
                    </div>
                </div>
                <div class="leaderboard">
                    <h6>Leaderboard</h6>
                    <div id="competition-leaderboard"></div>
                </div>
            </div>
        </div>
    `;
    agentHeader.appendChild(competitionToggle);
    
    // Initialize competition performance metrics
    const competitionStats = {
        totalCompetitions: 0,
        wins: {
            compliance: 0,
            data_analytics: 0, 
            project_management: 0,
            risk_forecasting: 0,
            systems_integration: 0,
            implementation_support: 0
        },
        corrections: {
            compliance: 0,
            data_analytics: 0, 
            project_management: 0,
            risk_forecasting: 0,
            systems_integration: 0,
            implementation_support: 0
        },
        responseTimes: {
            compliance: [],
            data_analytics: [], 
            project_management: [],
            risk_forecasting: [],
            systems_integration: [],
            implementation_support: []
        }
    };
    
    // Initialize charts
    let responseTimesChart = null;
    let winRateChart = null;
    
    // Toggle competition mode
    document.getElementById('competitionModeToggle').addEventListener('change', function(e) {
        competitionMode = e.target.checked;
        const dashboard = document.getElementById('competition-dashboard');
        
        if (competitionMode) {
            dashboard.style.display = 'block';
            initializeCompetitionCharts();
            addSystemMessage('Competition Mode', 'AI agents will now compete to provide the fastest and most accurate responses.');
        } else {
            dashboard.style.display = 'none';
            addSystemMessage('Standard Mode', 'Returning to standard query mode.');
        }
    });
    
    // Initialize competition charts
    function initializeCompetitionCharts() {
        const responseTimesCtx = document.getElementById('responseTimesChart').getContext('2d');
        const winRateCtx = document.getElementById('winRateChart').getContext('2d');
        
        // Colors for each agent
        const agentColors = {
            compliance: 'rgba(54, 162, 235, 0.7)',
            data_analytics: 'rgba(255, 99, 132, 0.7)',
            project_management: 'rgba(255, 206, 86, 0.7)',
            risk_forecasting: 'rgba(75, 192, 192, 0.7)',
            systems_integration: 'rgba(153, 102, 255, 0.7)',
            implementation_support: 'rgba(255, 159, 64, 0.7)'
        };
        
        // Response Times Chart
        if (responseTimesChart) {
            responseTimesChart.destroy();
        }
        
        responseTimesChart = new Chart(responseTimesCtx, {
            type: 'bar',
            data: {
                labels: Object.keys(agentNames).filter(name => name !== 'all'),
                datasets: [{
                    label: 'Average Response Time (s)',
                    data: Object.keys(competitionStats.responseTimes).map(agent => {
                        const times = competitionStats.responseTimes[agent];
                        return times.length > 0 ? times.reduce((a, b) => a + b, 0) / times.length : 0;
                    }),
                    backgroundColor: Object.values(agentColors)
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Seconds'
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Average Response Times'
                    }
                }
            }
        });
        
        // Win Rate Chart
        if (winRateChart) {
            winRateChart.destroy();
        }
        
        winRateChart = new Chart(winRateCtx, {
            type: 'doughnut',
            data: {
                labels: Object.keys(competitionStats.wins).map(id => agentNames[id]),
                datasets: [{
                    label: 'Win Rate',
                    data: Object.values(competitionStats.wins),
                    backgroundColor: Object.values(agentColors)
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Win Distribution'
                    }
                }
            }
        });
        
        // Update leaderboard
        updateLeaderboard();
    }
    
    // Update competition leaderboard
    function updateLeaderboard() {
        const leaderboard = document.getElementById('competition-leaderboard');
        
        // Create sorted leaderboard based on wins
        const entries = Object.entries(competitionStats.wins)
            .map(([agent, wins]) => ({
                agent,
                wins,
                corrections: competitionStats.corrections[agent],
                avgTime: competitionStats.responseTimes[agent].length > 0 
                    ? (competitionStats.responseTimes[agent].reduce((a, b) => a + b, 0) / 
                       competitionStats.responseTimes[agent].length).toFixed(2)
                    : 'N/A'
            }))
            .sort((a, b) => b.wins - a.wins);
        
        // Generate leaderboard HTML
        leaderboard.innerHTML = `
            <table class="table table-sm">
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Agent</th>
                        <th>Wins</th>
                        <th>Corrections</th>
                        <th>Avg Time</th>
                    </tr>
                </thead>
                <tbody>
                    ${entries.map((entry, index) => `
                        <tr>
                            <td>${index + 1}</td>
                            <td>${agentNames[entry.agent]}</td>
                            <td>${entry.wins}</td>
                            <td>${entry.corrections}</td>
                            <td>${entry.avgTime === 'N/A' ? entry.avgTime : entry.avgTime + 's'}</td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    }
    
    // Handle competition mode query
    function handleCompetitionQuery(message) {
        fetch('/api/compete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                query: message
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                addSystemMessage('Error', data.error);
            } else {
                // Update competition stats
                competitionStats.totalCompetitions++;
                competitionStats.wins[data.winner]++;
                competitionStats.responseTimes[data.winner].push(data.winning_time);
                
                if (data.correction_needed && data.correction_winner) {
                    competitionStats.corrections[data.correction_winner]++;
                }
                
                // Update charts if in competition mode
                if (competitionMode) {
                    initializeCompetitionCharts();
                }
                
                // Add winning response
                const winnerName = agentNames[data.winner];
                const winningResponseElement = addAgentMessage(data.winner, winnerName, data.winning_response, '100%');
                winningResponseElement.classList.add('winning-response');
                
                // Add competition metadata
                const metadata = document.createElement('div');
                metadata.className = 'competition-metadata';
                metadata.innerHTML = `<span class="winner-badge"><i class="bi bi-trophy"></i> Fastest Response (${data.winning_time.toFixed(2)}s)</span>`;
                winningResponseElement.querySelector('.message-header').appendChild(metadata);
                
                // Add analyses if there are any
                if (Object.keys(data.analyses).length > 0) {
                    const analysesContainer = document.createElement('div');
                    analysesContainer.className = 'analyses-container';
                    analysesContainer.innerHTML = `<h4>Other Agents' Analyses</h4>`;
                    
                    // Add collapsible container for analyses
                    const analysesContent = document.createElement('div');
                    analysesContent.className = 'analyses-content';
                    analysesContent.style.display = 'none';
                    
                    for (const [agentId, analysis] of Object.entries(data.analyses)) {
                        const analyzerName = agentNames[agentId];
                        const analysisElement = document.createElement('div');
                        analysisElement.className = 'analysis-item';
                        analysisElement.innerHTML = `
                            <div class="analysis-header">${analyzerName}</div>
                            <div class="analysis-content">${analysis}</div>
                        `;
                        analysesContent.appendChild(analysisElement);
                    }
                    
                    // Add toggle button
                    const toggleButton = document.createElement('button');
                    toggleButton.className = 'toggle-analyses-button';
                    toggleButton.innerHTML = 'Show Analyses';
                    toggleButton.addEventListener('click', function() {
                        const isVisible = analysesContent.style.display !== 'none';
                        analysesContent.style.display = isVisible ? 'none' : 'block';
                        toggleButton.innerHTML = isVisible ? 'Show Analyses' : 'Hide Analyses';
                    });
                    
                    analysesContainer.appendChild(toggleButton);
                    analysesContainer.appendChild(analysesContent);
                    winningResponseElement.appendChild(analysesContainer);
                }
                
                // Add correction if needed
                if (data.correction_needed) {
                    const correctionWinnerName = agentNames[data.correction_winner];
                    const correctionElement = addAgentMessage(data.correction_winner, correctionWinnerName, data.correction_response, '100%');
                    correctionElement.classList.add('correction-response');
                    
                    // Add correction metadata
                    const correctionMetadata = document.createElement('div');
                    correctionMetadata.className = 'competition-metadata correction';
                    correctionMetadata.innerHTML = `<span class="correction-badge"><i class="bi bi-exclamation-triangle"></i> Correction</span>`;
                    correctionElement.querySelector('.message-header').appendChild(correctionMetadata);
                }
            }
        })
        .catch(error => {
            console.error('Error:', error);
            addSystemMessage('Error', 'Failed to get a response. Please try again.');
        });
    }
});
