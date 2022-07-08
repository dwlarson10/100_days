
cdat_copy <- cdat%>%filter(unpaid > 0)


fit_bad_debt <- glm(unpaid ~ month+percILC+meanILC+meanECC, data = na.omit(cdat),family=Gamma)


tryCatch(
    glm(unpaid ~ month+percILC+meanILC+meanECC, data = na.omit(cdat),family=Gamma),
    error = function(c){ 
      message("error") 
      message(c)
     return(glm(unpaid ~ month, data = na.omit(cdat),family=Gamma))
      },
    warning = function(c) "warning",
    message = function(c) "message"
)
  

glm(rate ~ month + percILC + meanILC + meanECC, data = na.omit(cdat),family=Gamma)


glm(bad_debt_rate ~ month+percILC+meanILC+meanECC, data = na.omit(cdat),family=Gamma)  
  
  
glm(sd ~ portinflag2 ,data = dat_ilc,family = binomial(link='logit'))

logit_fit <- glm(sd ~ portinflag2 + ilc_ecc + device_price,data = dat,family = binomial(link='logit'))



fit <- glm(rate ~ month+percILC+meanILC+meanECC+mean_device_price, data = na.omit(cdat),family=Gamma(link="inverse"),start = c(.01,1,.75,2,2,500))
fit2 <- glm(bad_debt_rate ~ month+percILC+meanILC+meanECC+mean_device_price, data = na.omit(cdat),family=Gamma,start = c(.01,1,.75,2,2,500))
fit_bad_debt <- glm(unpaid ~ month + percILC + meanILC + meanECC , data = na.omit(cdat),family=Gamma,start = c(1,1,0.75,2,2))
fit_bad_debt <- glm(unpaid ~ month+percILC+meanILC+meanECC, data = na.omit(cdat),family=Gamma,start = c(1,1,.75,2,2))


