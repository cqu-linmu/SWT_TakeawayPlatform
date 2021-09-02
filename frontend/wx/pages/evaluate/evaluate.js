const { API } = require("../../utils/api");
Page({

    data: {
        order_id:1,
        evaluate_contant: ['给我们打个分吧！' ],
        stars: [0, 1, 2, 3, 4],
        normalSrc: '../../static/images/star/star.png',
        selectedSrc: '../../static/images/star/fill_star.png',
        halfSrc: '../../static/images/star/fill_half-star.png',
        score: 0,
        scores: [0],
    },
    onLoad:function(options) {
        this.setData({
            order_id:options.order_id
        })
    },
    // 提交事件
    submit_evaluate: function () {
        console.log('评价得分' + this.data.scores);
        let data={
            order_id:this.data.order_id,
            score:(this.data.scores[0]/5)
        }
        API.evaluate(data)
        .then(res=>{
            wx.navigateBack({
              delta: 0,
            })
            this.onUnload()
        })
        .catch(err=>{
            console.log("评价提交失败");
        });
    },

    //点击左边,半颗星
    selectLeft: function (e) {
        var score = e.currentTarget.dataset.score
        if (this.data.score == 0.5 && e.currentTarget.dataset.score == 0.5) {
            score = 0;
        }

        this.data.scores[e.currentTarget.dataset.idx] = score,
            this.setData({
                scores: this.data.scores,
                score: score
            })

    },

    //点击右边,整颗星
    selectRight: function (e) {
        var score = e.currentTarget.dataset.score

        this.data.scores[e.currentTarget.dataset.idx] = score,
            this.setData({
                scores: this.data.scores,
                score: score
            })
    }
})