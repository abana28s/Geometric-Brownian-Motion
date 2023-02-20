
library(shiny)
library(shinythemes)
library(pracma)

ui <- fluidPage(theme=shinytheme("yeti"),
                h1(id="big-heading", "Geometric Brownian Motion and Brownian Motion Generator"),
                tags$style(HTML("#big-heading{color: darkblue; 
                  font-size: 40px; 
                  font-style: normal; 
                  font-weight: 500; }")),
                
                sidebarLayout(
                  sidebarPanel(
                    tags$style(HTML("#input-heading{
                        color: darkblue; 
                        font-size: 20px; 
                        font-style: normal; 
                        font-weight: 400;}")),
                    selectInput(inputId = "gtype", label= h3(id = "input-heading","Select Graph Type") , c("Brownian Motion", "Geometric Brownian Motion")),
                    
                    
                    
                    numericInput(inputId = "sinit",
                                 label = h3(id = "input-heading", "So = (0,1000)"),
                                 value = 1,
                                 min = 0, 
                                 max = 1000),
                    
                    conditionalPanel(
                      condition = "input.gtype == 'Geometric Brownian Motion'", 
                      numericInput(inputId = "alpha",
                                   label = h3(id = "input-heading", "Mean (mu) {0,100}"),
                                   value = 1,
                                   min = 0, 
                                   max = 100),
                    ),
                    conditionalPanel(
                      condition = "input.gtype == 'Brownian Motion'", 
                      numericInput(inputId = "alpha",
                                   label = h3(id = "input-heading", "Drift (\U03B1) = (0,100)"),
                                   value = 1,
                                   min = 0, 
                                   max = 100),
                    ),
                    
                    conditionalPanel(
                      condition = "input.gtype == 'Geometric Brownian Motion'", 
                      numericInput(inputId = "sigma",
                                   label = h3(id = "input-heading", "Standard Deviation (sigma) {0,50}"),
                                   value = 1,
                                   min = 0, 
                                   max = 50),
                    ),
                    conditionalPanel(
                      condition = "input.gtype == 'Brownian Motion'", 
                      numericInput(inputId = "sigma",
                                   label = h3(id = "input-heading", "Volatility (\U03C3) = (0,50)"),
                                   value = 1,
                                   min = 0, 
                                   max = 50),
                    ),
                    
                    
                    conditionalPanel(
                      condition = "input.gtype == 'Geometric Brownian Motion'", 
                      sliderInput(inputId = "time",
                                  label = h3(id = "input-heading", "Time (T)"),
                                  min = 0,
                                  max = 10,
                                  value = 1),
                    ),
                    conditionalPanel(
                      condition = "input.gtype == 'Brownian Motion'", 
                      sliderInput(inputId = "time",
                                  label = h3(id = "input-heading", "Time (T)"),
                                  min = 0,
                                  max = 50,
                                  value = 30),
                    ),
                    
                    
                    sliderInput(inputId = "steps",
                                label = h3(id = "input-heading", "No of Steps (s)"),
                                min = 0,
                                max = 2000,
                                step = 200,
                                value = 1015),
                    
                    
                    
                  ),
                  
                  mainPanel(
                    h2(id = "plot-heading", "The generated plot for chosen values  "), 
                    tags$style(HTML("#plot-heading{color: black; font-size: 25px; font-weight: 500;}")),
                    plotOutput(outputId = "plot")
                    
                  )
                )
)

server <- function(input, output) {
  
  output$plot <- renderPlot({
    
    gtype <- input$gtype
    a <- input$alpha
    s <- input$sigma
    stps <- input$steps
    delta <- input$time/stps
    Time <- linspace(0, input$time, stps+1)
    
    curr <- input$sinit
    if(gtype == "Brownian Motion"){
      Value <- c(curr)
      for (i in 1:stps)
      {
        curr <- curr+ a*delta + s*sqrt(delta)*rnorm(1)
        Value <- append(Value,curr)
      }
      plot(Time, Value, type='l', col="seagreen", lwd=2.5)
    }
    else{
      Value <- c(curr)
      for (i in 1:stps)
      {
        curr <- curr*exp((a-(s*s)/2)*delta + s*sqrt(delta)*rnorm(1)) 
        Value <- append(Value,curr)
      }
      plot(Time, Value, type='l', col="seagreen", lwd = 2.5)
    }
    
    
  })
  
}

shinyApp(ui = ui, server = server)