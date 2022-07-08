
library(shiny)
require(spotifyr)
require(tidyverse)
require(ggplot2)
require(tidytext)
require(ggbeeswarm)
require(highcharter)



Sys.setenv(SPOTIFY_CLIENT_ID = 'c9eb9c91c7d54df9815c742543687f54')
Sys.setenv(SPOTIFY_CLIENT_SECRET = '9778531b27614720be4f7c5224a9c975')
access_token <- get_spotify_access_token()



# Define UI for application that draws a histogram
ui <- fluidPage(

    # Application title
    titlePanel("Know an artist's catalog"),

    # Sidebar with a slider input for number of bins 
    sidebarPanel(
        h1("Who is your fav artist?"),
            fluidRow(
                column(6, textInput("search_string", "Which Artist", "Kanye West"))
            ),
        h1("Albums"),
        uiOutput("imageGrid"),
        tags$script(HTML(
            "$(document).on('click', '.clickimg', function() {",
            "  Shiny.onInputChange('clickimg', $(this).data('value'));",
            "};"
        )),
        h1("Distribution of track key"),
        plotOutput("distKey")
        ),

        # Show a plot of the generated distribution
        mainPanel(
           
           plotOutput("distMetric"),
           highchartOutput("distCor")
        )
    )

# Define server logic required to draw a histogram
server <- function(input, output) {
    
    get_track <- reactive({
    
         df <- get_artist_audio_features(input$search_string)
         return(df)
    })
    

    output$distKey <- renderPlot({
        # generate bins based on input$bins from ui.R
        df <- get_track()
        
        df%>%group_by(key_name)%>%summarise(count=n())%>%
            ggplot(aes(x=reorder(key_name,count),y=count,fill=key_name))+
          geom_bar(stat='identity')+
          coord_flip()+
            theme_minimal()+
          ggtitle('Number of tracks in the key of')
    })
    
    output$distMetric <- renderPlot({
        # generate bins based on input$bins from ui.R
        df2 <- get_track()
        
        df2%>%select('track_name','danceability',
                    'energy', 'speechiness', 'acousticness', "instrumentalness", 'liveness', 'valence')%>%
            gather(key='metric',value = 'value',-track_name)%>%
            ggplot(aes(x=value,y=metric,color=metric))+
            geom_quasirandom(groupOnX=FALSE)+
            theme_minimal()+
          ggtitle('Distribution of track metrics. ')
    })
    
    output$distMetric <- renderPlot({
      # generate bins based on input$bins from ui.R
      df2 <- get_track()
      
      df2%>%select('track_name','danceability',
                   'energy', 'speechiness', 'acousticness', "instrumentalness", 'liveness', 'valence')%>%
        gather(key='metric',value = 'value',-track_name)%>%
        ggplot(aes(x=value,y=metric,color=metric))+
        geom_quasirandom(groupOnX=FALSE)+
        theme_minimal()+
        ggtitle('Distribution of track metrics. ')
    })
    
    output$distCor <- renderHighchart({
      # generate bins based on input$bins from ui.R
      df2 <- get_track()
      
      
      hchart(cor(df %>% select('danceability',
                               'energy', 'speechiness', 'acousticness', "instrumentalness", 'liveness', 'valence'))) 
      
      
    })

output$imageGrid <- renderUI({
    df <- get_track()
    pic_1 <- map_df(df$album_images,unnest)%>%filter(width==64)%>%unique()
    
    fluidRow(
        lapply(pic_1$url, function(img) {
            column(3, 
                   tags$img(src=img, class="clickimg", value=img)
            )
        })
    )
})

}

# Run the application 
shinyApp(ui = ui, server = server)
