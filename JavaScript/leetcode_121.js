function maxProfit(prices){
    let maxProfit = 0
    let minPrice = prices[0]
    for (let i = 0 ; i < prices.length ; i++){
        let sellPrice = prices[i]
        let profit = sellPrice - minPrice

        maxProfit = Math.max(maxProfit, profit)
        if(sellPrice < minPrice)
            minPrice = sellPrice
    }
    return maxProfit
}