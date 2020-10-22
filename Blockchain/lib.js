const Web3 = require('web3')

var web3, account

class Contract {
    constructor(address, abi) {
        this.address = address
        this.abi = abi
        this.object = new web3.eth.Contract(abi, address)
    }

    async view(name, ...args) {
        return await this.object.methods[name](...args).call()
    }

    async call(tx, name, ...args) {
        if (typeof tx === 'string') {
            if (name) {
                args = [name, ...args]
            }
            name = tx
        }
        let func = this.object.methods[name](...args)
        let s = await web3.eth.accounts.signTransaction({
            to: this.address,
            data: func.encodeABI(),
            nonce: await web3.eth.getTransactionCount(account.address),
            gasLimit: 1000000,
            ...tx
        }, account.privateKey)
        await new Promise((resolve, reject) => {
            web3.eth.sendSignedTransaction(s.rawTransaction)
                .on('transactionHash', (txHash) => {
                    console.log(`Transaction -> https://ropsten.etherscan.io/tx/${txHash}`)
                })
                .on('error', reject)
                .then(resolve)
        })
    }

    async storage(position) {
        return await web3.eth.getStorageAt(this.address, position)
    }
}

module.exports = function (config) {
    web3 = new Web3(config.network)
    account = config.account
    return {
        web3: web3,
        account: account,
        contract: function (address, abi) {
            return new Contract(address, abi)
        }
    }
}
